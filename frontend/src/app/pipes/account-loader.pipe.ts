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
        const name = this.account.getName();
        return (name === undefined ? value : name);
      default:
        return value;
    }
  }

}
