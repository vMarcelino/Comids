import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { AppSettings } from "../../shared/constants";

@Component({
    selector: 'app-purchased',
    templateUrl: './purchased.component.html',
    styleUrls: ['./purchased.component.css', '../homePage/blank.materialize.min.css', '../homePage/blank.materialize.css']
})
export class PurchasedComponent {
    Items: Object[] = []
    Value = 0
    constructor(private http: HttpClient) {

        var order_id = window.localStorage.getItem('order_id')
        var token = window.localStorage.getItem('user_token')
        this.http.get(AppSettings.API_ENDPOINT + 'order', { 'params': { 'order_id': order_id, 'token': token } })
            .subscribe(
                data => {
                    console.log(data)
                    this.Items = []
                    data = data['items']

                    this.Value = 0
                    Object.keys(data).forEach(index => {
                        console.log(data[index])
                        this.Items.push(data[index])
                        this.Value += data[index]['value']
                    });
                },
                error => {
                    console.log(error)
                    alert('Erro: falha ao listar itens')
                }
            )
    }

}