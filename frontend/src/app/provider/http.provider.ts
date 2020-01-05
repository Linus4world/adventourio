import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../environments/environment';
import { Observable } from 'rxjs';

/**
 * This service is a wrapper for the angular http provider to simplify the communication with the backend (configured in envirnment.ts)
 */
@Injectable()
export class HTTP {
    private headers = new HttpHeaders();
    private options = {headers: this.headers};
    constructor(private http: HttpClient) {
        this.headers.append('content-type', 'text/plain');
    }

    /**
     * Performs a GET request to the REST API of the backend
     * @param url sub URL on the backend (does not start with /)
     */
    public GET(url: string): Observable<any> {
        return this.http.get(environment.serverURL + url);
    }

    /**
     * Performs a POST request to the REST API of the backend
     * @param url sub URL on the backend (does not start with /)
     * @param body payload of the request
     */
    public POST(url: string, body: string): Observable<any> {
        return this.http.post(environment.serverURL + url, body, this.options);
    }

    /**
     * Performs a PATCH request to the REST API of the backend
     * @param url sub URL on the backend (does not start with /)
     * @param body payload of the request
     */
    public PATCH(url: string, body: string): Observable<any> {
        return this.http.post(environment.serverURL + url, body, this.options);
    }
}
