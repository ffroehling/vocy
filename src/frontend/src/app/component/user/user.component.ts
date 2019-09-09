import { Component, OnInit } from '@angular/core';
import { UserService } from '../../services/user/user.service'
import { User } from '../../model/user'
import { GridComponent } from '../grid/grid.component';
import {Router} from '@angular/router';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css']
})
export class UserComponent implements OnInit {
    private user : User[];

    constructor(private userService : UserService, private router : Router) {
        console.log('Loading');
        userService.loadUser().then((user) => {
            this.user = user;
        });
    }

  ngOnInit() {

  }

  on_user_select(user){
      console.log(user);
      this.userService.setActiveUser(user);
      this.router.navigateByUrl('/lists');
  }

}
