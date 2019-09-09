import { Component, ElementRef, Input, OnInit, OnDestroy, TemplateRef} from '@angular/core';

@Component({
  selector: 'app-grid',
  templateUrl: './grid.component.html',
  styleUrls: ['./grid.component.css']
})
export class GridComponent implements OnInit {
    @Input() click : any;
    @Input() template : TemplateRef<any>;
    @Input() dataset : any;

    ctx = {
        name : 'asdf'
    }
    private element : ElementRef;

    constructor(private el: ElementRef) {
        this.element = el.nativeElement;
        console.log(this.element);
    }

    ngOnInit() {
        console.log(this.dataset);
        console.log(this.click);
    }

}
