import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { LanguagePairComponent } from './component/language-pair/language-pair.component';
import { RouterModule, Routes } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';
import {HttpErrorHandlerService} from './services/http-error-handler.service';
import {ModalComponent} from './directive/modal.directive';
import { ModalService } from './services/modal/modal.service';
import { LanguageListComponent } from './component/language-list/language-list.component';

const appRoutes: Routes = [
  { path: 'languagepairs', component: LanguagePairComponent }
];

@NgModule({
  declarations: [
    AppComponent,
    LanguagePairComponent,
    ModalComponent,
    LanguageListComponent
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(
      appRoutes,
      { enableTracing: true } // <-- debugging purposes only
    ),
    HttpClientModule
  ],
  providers: [HttpErrorHandlerService, ModalService],
  bootstrap: [AppComponent]
})
export class AppModule { }
