import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { GoogleSigninService } from './gogle-singin.servis';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
})
export class AppComponent implements OnInit {
    title = 'Google.Signin';

    user: gapi.auth2.GoogleUser

    constructor(private signInService: GoogleSigninService, private ref : ChangeDetectorRef){
        
    }

    ngOnInit(): void {
        this.signInService.observable().subscribe ( user => {
            this.user = user
            this.ref.detectChanges()


        })     
    }

    signIn () {
        this.signInService.signIn()
    }

    signOut () {
        this.signInService.signOut()
    }
}
