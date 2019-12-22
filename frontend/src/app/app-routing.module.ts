import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';

const routes: Routes = [
  {
    path: '',
    children: [
      {
        path: 'tab1', loadChildren: './tab1/tab1.module#Tab1PageModule'
      },
      {
        path: 'tab2', loadChildren: './tab2/tab2.module#Tab2PageModule'
      },
      {
        path: 'tab3', loadChildren: './tab3/tab3.module#Tab3PageModule'
      },
      {
        path: '',
        redirectTo: '/tab1',
        pathMatch: 'full'
      }
    ]
  }
];
@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule {}
