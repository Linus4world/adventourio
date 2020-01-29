import { Pipe, PipeTransform } from '@angular/core';
import { Account } from '../provider/account.provider';

@Pipe({
  name: 'accountLoader'
})
export class AccountLoaderPipe implements PipeTransform {

  constructor(private account: Account) { }

  transform(value: string, ...args: any[]): any {
    const ret = this.account.get(value);
    return ret === undefined ? value.toUpperCase() : ret;
  }

}
