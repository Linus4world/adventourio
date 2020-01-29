import { Injectable } from '@angular/core';
import { HTTP } from './http.provider';
import { Observable } from 'rxjs';
import { Account, AccountValue } from './account.provider';
import { map } from 'rxjs/operators';
import { Questionnaire, QuestionnaireAnswers, Stage, ChallengeOutcome } from './models';
import { GeolocationProvider } from './geolocation.provider';

/**
 * This service takes care of all high-level game mechanics.
 */
@Injectable()
export class GameProvider {
    private MAX_TIMEOUT = 60000;
    private character = 'Adventurer';

    constructor(private http: HTTP, private account: Account, private geolocationProvider: GeolocationProvider) { }

    /**
     * Retrieves the questionnaire from the server
     */
    public loadQuestionnaire(): Observable<Questionnaire> {
        return this.http.GET('questionnaire');
    }

    /**
     * Sends the answers of the questionnaire back to server
     * @param answers Array of answers on string format
     */
    public sendQuestionnaireAnswers(answers: QuestionnaireAnswers): Observable<void> {
        return this.http.POST('join/' + this.account.getID(), JSON.stringify(answers), this.MAX_TIMEOUT).pipe(
            map((response: { playerNames: string[], character?: string}) => {
                console.log('Players in session: ', response.playerNames);
                const friends = this.account.getFriends();
                for (const friend of response.playerNames) {
                    if (friend !== this.account.getName() && friends.indexOf(friend) < 0) {
                        friends.push(friend);
                    }
                }
                this.character = response.character;
                this.account.store(AccountValue.friends, friends);
            })
        );
    }

    /**
     * Signals the server that the current quest was finished and asks for the next quest.
     */
    public getNextQuest(challengeOutcome?: boolean, playerLocation?: number[]): Observable<Stage> {
        const data: ChallengeOutcome = {
            challengeOutcome,
            playerLocation
        };
        return this.http.POST('stage/' + this.account.getID(), JSON.stringify(data));
    }

    public unlockChallenge() {
        return this.http.GET('here/<id>' + this.account.getID(), this.MAX_TIMEOUT);
    }

    public getCharacter(): string {
        return this.character;
    }
}
