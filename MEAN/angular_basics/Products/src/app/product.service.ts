import { Injectable } from '@angular/core';
import 'rxjs'
import { BehaviorSubject } from 'rxjs/BehaviorSubject'


@Injectable()
export class ProductService {

  productObservable = new BehaviorSubject(null);

  updatedList(products: Array<any>){
    this.productObservable.next(products);
  };

  constructor() { }

}
