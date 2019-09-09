import { Component, OnInit } from '@angular/core';
//import {LanguageService} from '../../services/language.service';
//import { Languagepair } from '../../model/languagepair';
//import { ModalService} from '../../services/modal/modal.service';

@Component({
  selector: 'app-language-pair',
  templateUrl: './language-pair.component.html',
  styleUrls: ['./language-pair.component.css']
})
export class LanguagePairComponent implements OnInit {

    /*private language_pairs : Languagepair[];

  constructor(private language_service : LanguageService, private modalService : ModalService) { 
    var that = this;

    language_service.loadLanguagePairs().then(function(response){
      that.language_pairs = response;
      console.log(response);
    })
  }

  openModal(id : string){
    this.modalService.open(id);
  }

  closeModal(id : string){
    this.modalService.close(id);
  }*/

  ngOnInit() {}
    constructor(){
    }

}
