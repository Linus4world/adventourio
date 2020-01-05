import { RouterModule } from '@angular/router';
import { NgModule } from '@angular/core';
import { OpenlayerComponent } from './openlayer.component';

@NgModule({
  imports: [
    RouterModule.forChild([{ path: '', component: OpenlayerComponent }])
  ],
  declarations: [OpenlayerComponent],
  exports: [OpenlayerComponent]
})
export class OpenlayerModule {}
