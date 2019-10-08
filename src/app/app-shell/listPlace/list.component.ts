import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
    selector: 'app-list',
    templateUrl: './list.component.html',
    styleUrls: ['./list.component.css', '../homePage/blank.materialize.css']
})
export class ListComponent {
    Places: string[] = ['p1', 'p2']
    constructor(private http: HttpClient) {

        var ip = 'eisengarth.ddns.net'
        var ip = '127.0.0.1'
        this.http.get('http://' + ip + ':2283/place/list')
            .subscribe(
                data => {
                    console.log(data)
                    this.Places = []
                    Object.keys(data).forEach(key => {
                        data[key]['id'] = key
                        this.Places.push(data[key])
                        window.localStorage.setItem('place_id', key.toString())
                    });
                },
                error => {
                    alert('Erro: login incorreto')
                }
            )
    }
    OnInit() {

    }
}
