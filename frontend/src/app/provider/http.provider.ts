import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';
import { Observable } from 'rxjs';

@Injectable()
export class HTTP {
    private options;
    constructor(private http: HttpClient) {}

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
