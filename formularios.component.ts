import { group } from '@angular/animations';
import { Component, OnInit } from '@angular/core';
import { FormBuilder,FormGroup, Validators} from '@angular/forms';

@Component({
  selector: 'app-formularios',
  templateUrl: './formularios.component.html',
  styleUrls: ['./formularios.component.css']
})
export class FormulariosComponent implements OnInit {
  title = 'Generador de horarios';
  contactForm!: FormGroup;

  constructor(private readonly fb: FormBuilder) { }

  ngOnInit(): void {
    this.contactForm = this.initForm();
  }

  onSubmit(): void{
    console.log('Form ->');
  }

  initForm(): FormGroup {
    return this.fb.group({
      carrera:['', [Validators.required , Validators.minLength(1)]],
      coordinador:['', [Validators.required , Validators.minLength(1)]],
      aPaterno:['', [Validators.required , Validators.minLength(1)]],
      aMaterno:['', [Validators.required , Validators.minLength(1)]],
      email:['', [Validators.required , Validators.minLength(1)]]
    });
    
  }

}
