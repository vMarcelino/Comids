import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { AppSettings } from "../../shared/constants";
import { Router } from '@angular/router';

@Component({
    selector: 'app-master-detail',
    templateUrl: './master-detail.component.html',
    styleUrls: ['./master-detail.component.css', '../homePage/blank.materialize.min.css', '../homePage/blank.materialize.css']
})
export class MasterDetailComponent {
    Items: Object[] = []
    constructor(private http: HttpClient, public router: Router) {

        var place_id = window.localStorage.getItem('place_id')
        this.http.get(AppSettings.API_ENDPOINT + 'place/menu/list/' + place_id)
            .subscribe(
                data => {
                    console.log(data)
                    this.Items = []
                    Object.keys(data).forEach(key => {
                        this.http.get(AppSettings.API_ENDPOINT + 'menu/' + key)
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
                                    alert('Erro: falha ao listar items dos menus')
                                }
                            )

                    });
                },
                error => {
                    alert('Erro: falha ao listar menus')
                }
            )
    }

    onItemClicked(item_id) {
        var token = window.localStorage.getItem('user_token')
        var place_id = window.localStorage.getItem('place_id')
        this.http.get(AppSettings.API_ENDPOINT + 'order', { 'params': { 'place_id': place_id, 'token': token } })
            .subscribe(
                data => {
                    console.log('orders from place:')
                    console.log(data)
                    var keys = Object.keys(data)
                    var size = keys.length;
                    if (size == 0) {
                        console.log('Creating order')
                        this.http.post(AppSettings.API_ENDPOINT + 'order', { 'place_id': place_id, 'item_id': item_id, 'token': token })
                            .subscribe(data2 => {
                                console.log('order creation response:')
                                console.log(data2)
                                this.router.navigate(['purchased'])
                            },
                                error => {
                                    console.log(error)
                                    alert('Erro: Falha ao criar ordem de compra')
                                })
                    }
                    else {
                        var order_id = keys[0]
                        console.log('Using order ' + order_id.toString())
                        this.http.put(AppSettings.API_ENDPOINT + 'order', {
                            'order_id': order_id, 'item_id': item_id, 'token': token
                        })
                            .subscribe(data2 => {
                                console.log('item add response:')
                                console.log(data2)
                                this.router.navigate(['purchased'])
                            },
                                error => {
                                    console.log(error)
                                    alert('Erro: Falha ao adicionar item à ordem de compra')
                                })
                    }
                },
                error => {
                    console.log(error)
                    alert('Erro: Falha ao listar ordem de compra')
                }
            )
    }
}

