import { Component, OnInit, OnDestroy } from '@angular/core';
import { ProductService } from './../product.service';
import { Router, ActivatedRoute } from '@angular/router';
import { Product } from './../product';
import { Subscription } from 'rxjs/Subscription';

@Component({
  selector: 'app-edit',
  templateUrl: './edit.component.html',
  styleUrls: ['./edit.component.css']
})

export class EditComponent implements OnInit {

  subscription: Subscription;
  products: Array<Product> = [];
  currProduct: Product;

  constructor(private _productService: ProductService, private _route: ActivatedRoute, private _router: Router) { 
    this.subscription = this._productService.productObservable.subscribe(
        (data) => {
            this.products = data;
        }
    )
    this._route.params.subscribe((param) => {
      console.log(param.id)
        for(let i = 0; i < this.products.length; i++) {
            if(this.products[i].id == param.id) {
                this.currProduct = this.products[i];
            }
        }   
    })
  }

  ngOnInit() {
  }

  delete(){
    
  }

  updateProducts(){
    this._productService.updatedList(this.products);
    this._router.navigate(['/products']);
  }

  deleteProduct(){
    for(let i = 0; i < this.products.length; i++){
      if(this.products[i].id == this.currProduct.id){
        this.products.splice(i,1);
      }
      this._router.navigate(['/products']);
    }
  }

  onDestroy() {
    this.subscription.unsubscribe();
  }
  


}
