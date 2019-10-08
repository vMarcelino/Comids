import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
    selector: 'app-list',
    templateUrl: './list.component.html',
    styleUrls: ['./list.component.css', '../homePage/blank.materialize.css']
})
export class ListComponent {
    Places: Object[] = ['p1', 'p2']
    constructor(private http: HttpClient, public router: Router) {

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

                    });
                },
                error => {
                    alert('Erro: login incorreto')
                }
            )
    }
    onPlaceClicked(place_id) {
        window.localStorage.setItem('place_id', place_id.toString())
        this.router.navigate(['listItem'])
    }
}
