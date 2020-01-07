import { Pipe, PipeTransform } from '@angular/core';
import { Account } from '../provider/account.provider';

@Pipe({
  name: 'accountLoader'
})
export class AccountLoaderPipe implements PipeTransform {

  constructor(private account: Account) {}

  transform(value: any, ...args: any[]): any {
    switch (value) {
      case 'NAME':
        return this.account.getName();
      default:
        return null;
    }
  }

}
