import { Component, OnInit, OnDestroy } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { ProductService } from './../product.service';
import { Subscription } from 'rxjs/Subscription';
import { Product } from './../product'

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.css']
})
export class ListComponent implements OnInit {

  subscription: Subscription;
  products: Array<any> = [];

  constructor(private _productService: ProductService, private _route: Router) { 
    this.subscription = _productService.productObservable.subscribe(
      (data) => { this.products = data, console.log(data) },
      (err) => { console.log("1"); },
      () => { }
    )
  }

  ngOnInit() {
  }
  
  delete(idx){
    this.products.splice(idx, 1);
  }

  updatedList(){
    this._productService.updatedList(this.products);
  }

  onDestroy() {
    this.subscription.unsubscribe();
  }

}
