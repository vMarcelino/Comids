import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
    selector: 'app-master-detail',
    templateUrl: './master-detail.component.html',
    styleUrls: ['./master-detail.component.css', '../homePage/blank.materialize.min.css', '../homePage/blank.materialize.css']
})
export class MasterDetailComponent {
    Items: Object[] = []
    constructor(private http: HttpClient) {

        var ip = 'eisengarth.ddns.net'
        var ip = '127.0.0.1'
        var place_id = window.localStorage.getItem('place_id')
        this.http.get('http://' + ip + ':2283/place/menu/list/' + place_id)
            .subscribe(
                data => {
                    console.log(data)
                    this.Items = []
                    Object.keys(data).forEach(key => {
                        this.http.get('http://' + ip + ':2283/menu/' + key)
                            .subscribe(
                                data2 => {
                                    data2 = data2['items']
                                    console.log(data2)
                                    Object.keys(data2).forEach(key2 => {
                                        data2[key2]['id'] = key2
                                        this.Items.push(data2[key2])
                                    });
                                },
                                error => {
                                    alert('Erro: login incorreto')
                                }
                            )

                    });
                },
                error => {
                    alert('Erro: login incorreto')
                }
            )
    }
}

// this.http.get('http://' + ip + ':2283/place/menu/list/' + place_id)
//             .subscribe(
//                 data => {
//                     console.log(data)
//                     this.Items = []
//                     Object.keys(data).forEach(key => {
//                         data[key]['id'] = key
//                         this.Items.push(data[key])
//                         window.localStorage.setItem('place_id', key.toString())
//                     });
//                 },
//                 error => {
//                     alert('Erro: login incorreto')
//                 }
//             )