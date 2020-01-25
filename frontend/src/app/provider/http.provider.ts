import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../environments/environment';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';

/**
 * This service is a wrapper for the angular http provider to simplify the communication with the backend (configured in envirnment.ts)
 */
@Injectable()
export class HTTP {
    private headers = {
        'content-type': 'application/json'
    };
    private options = {headers: undefined};
    constructor(private http: HttpClient) {
        this.options.headers = new HttpHeaders(this.headers);
    }

    /**
     * Performs a GET request to the REST API of the backend. Make sure to subscribe to the observable!
     * @param url sub URL on the backend (does not start with /)
     * @param timeout Number of milliseconds before the request will timeout
     */
    public GET(url: string, timeout?: number): Observable<any> {
        console.log('GET', environment.serverURL + url);
        if (timeout) {
            const headers = new HttpHeaders(this.headers);
            headers.append('timeout', '' + timeout);
            return this.http.get(environment.serverURL + url, {headers});
        }
        return this.http.get(environment.serverURL + url, this.options);
    }

    /**
     * Performs a POST request to the REST API of the backend
     * @param url sub URL on the backend (does not start with /)
     * @param body payload of the request
     */
    public POST(url: string, body: string, timeout?: number): Observable<any> {
        console.log('POST', environment.serverURL + url, body);
        if (timeout) {
            const headers = new HttpHeaders(this.headers);
            headers.append('timeout', '' + timeout);
            return this.http.post(environment.serverURL + url, body, {headers});
        }
        return this.http.post(environment.serverURL + url, body, this.options);
    }

    /**
     * Performs a PATCH request to the REST API of the backend
     * @param url sub URL on the backend (does not start with /)
     * @param body payload of the request
     */
    public PATCH(url: string, body: string): void {
        this.http.post(environment.serverURL + url, body, this.options).subscribe(_ => undefined, error => console.log(error));
    }
}
