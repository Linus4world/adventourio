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
        return this.http.GET('/join/' + this.account.getID(), 60000).pipe(map((response: HttpResponse<any>) => {
            this.session = response.body;
            return this.session;
        }));
    }
}
