import { Component, OnInit, OnDestroy } from '@angular/core';
import { Product } from './../product'
import { ProductService } from './../product.service'
import { Router, ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.css']
})
export class CreateComponent implements OnInit {

  item1: Product = new Product(1,'GameBoy',80)
  products: Array<Product> = [this.item1];
  newProduct: Product = new Product();

  constructor(
    private _productService: ProductService,
    private _router: Router
  ){
    _productService.updatedList(this.products);
  }

  ngOnInit() {
    this.newProduct = new Product();
  }

  addItem(){
    this.products.push(this.newProduct);
    this._productService.updatedList(this.products);
    this.newProduct = new Product();
    this._router.navigate(['/products']);
  }

  updatedList(){
    this._productService.updatedList(this.products);
  }

}
