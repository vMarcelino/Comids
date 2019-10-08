import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import {AppSettings}from '../../shared/constants'

@Component({
    selector: 'app-blank',
    templateUrl: './blank.component.html',
    styleUrls: ['./blank.component.css', './blank.materialize.min.css']
})
export class BlankComponent {
    @ViewChild('passwordinput', { static: false }) passwordInput: ElementRef
    @ViewChild('userinput', { static: false }) userInput: ElementRef
    constructor(private http: HttpClient, public router: Router) { }
    onLoginClicked(event: Event) {
        var user = this.userInput.nativeElement.value
        var password = this.passwordInput.nativeElement.value
        var data = { 'user': user, 'password': password }
        console.log(user + ', ' + password)
        this.http.post(AppSettings.API_ENDPOINT+ 'auth', data)
            .subscribe(
                data => {
                    console.log(data)
                    var token = data['token']
                    console.log(token)
                    window.localStorage.setItem('user_token', token)
                    this.router.navigate(['listPlace'])
                },
                error => {
                    alert('Erro: login incorreto')
                }
            )
    }
}
