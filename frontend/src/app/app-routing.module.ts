import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';
import { LoadingGuard } from './provider/loading-guard.provider';

const routes: Routes = [
  {
    path: '',
    children: [
      {
        path: 'start', loadChildren: './start/start.module#StartPageModule'
      },
      {
        path: 'q', loadChildren: './questionaire/questionaire.module#QuestionaireModule'
      },
      {
        path: 'tab1', loadChildren: './tab1/tab1.module#Tab1PageModule', canLoad: [LoadingGuard]
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
