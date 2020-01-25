import { Injectable } from '@angular/core';
import { HTTP } from './http.provider';
import { Observable } from 'rxjs';
import { Account } from './account.provider';
import { HttpResponse } from '@angular/common/http';
import { map } from 'rxjs/operators';

export interface Session {
    id: string;
    players: string[];
}

export interface Questionnaire {
    questions: [
        {
            id: number,
            question: string,
            answers: string
        }
    ];
}

export interface QuestionnaireAnswers {
    name: string;
    answers: string[];
}

export interface  Quest {
    story: string[];
    goalLocation: number[];
    challenge: Challenge;
}

export interface Challenge {
    challenge: string;
    challenge_type: number;
    answers?: string[];
    right_answer: string | number[];
}

/**
 * This service takes care of all high-level game mechanics.
 */
@Injectable()
export class GameProvider {

    private session: Session;

    constructor(private http: HTTP, private account: Account) {}

    /**
     * Sends a request to server to join a Session. The server will wait until enough players joined the session.
     * Then it sends back the session information. If not enough players joined the lobby within the timeout, the Observable will respond
     * with an undefined
     */
    public lookingForPlayers(): Observable<Session> {
        return this.http.GET('join/' + this.account.getID(), 60000).pipe(map((response: HttpResponse<any>) => {
            this.session = response.body;
            return this.session;
        }));
    }

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
    public sendQuestionnaireAnswers(answers: QuestionnaireAnswers) {
        return this.http.POST('questionnaire', JSON.stringify(answers));
    }

    /**
     * Signals the server that the current quest was finished and asks for the next quest.
     */
    public getNextQuest(): Observable<Quest> {
        return this.http.GET('quest/' + this.account.getID());
    }
}
