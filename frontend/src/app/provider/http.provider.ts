import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../environments/environment';
import { Observable } from 'rxjs';

@Injectable()
export class HTTP {
    private headers = new HttpHeaders();
    private options = {headers: this.headers};
    constructor(private http: HttpClient) {
        this.headers.append('content-type', 'text/plain');
    }

    public GET(url: string): Observable<any> {
        return this.http.get(environment.serverURL + url);
    }

    public POST(url: string, body: string): Observable<any> {
        return this.http.post(environment.serverURL + url, body, this.options);
    }

    public PATCH(url: string, body: string): Observable<any> {
        return this.http.post(environment.serverURL + url, body, this.options);
    }
}
