
const init_capcha=(self)=>{
    fetch('/capcha?action=out_key&json=1')
    .then(function (response) {
        response.text().then(function (data) {
            data = JSON.parse(data);
            self.form_capture_key = data.capture_key;
            self.form_capture_src = data.capture_src;
        })
        .catch(function (err) {
            setTimeout(()=>{ init_capcha(self)},1000);
        })
    })
}

const check_form=(self)=>{
    let exists_errors=false
    for(let f of self.check_fields){
      
      if('check' in f){
        let v=self[f.name], err=f.check(v)

        if(err){
          self.error[f.name]=err, exists_errors=true
        }
      }
    }
    
    return exists_errors
}

const clear_errors=(self)=>{
    for(let e in self.error ) self.error[e]=''
}
const func_not_empty=(v)=>{return (v.length?'':'пожалуйста заполните поле')}
const func_name_check=(v)=>{return v?'':'пожалуйста представьтесь'};
const func_phone_check=(v)=>{
    s=v+'';
    s=s.replace(/[^0-9]/g,'');
    if(!s)
        return 'заполните поле'
    return (s.length < 9)?'укажите телефон в формате: +7 (XXX) XXX-XX-XX':''
};
const func_email_check=(v)=>{
    if(!v){
      return 'email не указан'
    }
    if(/^[a-zA-Z0-9\-_\.]+@[a-zA-Z0-9\-_\.]+\.[a-zA-Z0-9\-_\.]+$/.test(v)){
      return ''
    }
    return 'email заполнен не корректно'
}
const func_dat_check=v=>{
    return ''
}
const func_replace_phone=(v)=>{
    v=v.replace(/[^\d]/g,'');
    v=v.replace(/^(\d{11}).+$/g,'$1');
    v=v.replace(/^[87]/,'+7');
    v=v.replace(/^\+7(\d{3})(\d)/,"+7 ($1) $2");
    v=v.replace(/^(\+7 \(\d{3}\))(\d{3})/,"$1 $2");
    v=v.replace(/(\d{3})(\d{2})/,"$1-$2");
    v=v.replace(/(\d{2})(\d{2})/,"$1-$2");
    return v
}
const getById=id=>{
    return document.getElementById(id)
}

let app_modal_consultation=new Vue({
    el:'#modal_consultation',
    data:{
        form_capture_key:'',form_capture_src:'',form_capture_str:'',
        name:'',email:'',phone:'',service:'',dat:'',address:'',message:'',
        check_fields:[
            {name:'name','check': func_name_check},
            {name:'phone','check': func_phone_check},
            {name:'email','check': func_email_check},
            {name:'message','check': func_not_empty},
        ],
        error:{
            name:'',phone:'',email:'',message:'',form_capture_str:''
        }
    },
    created(){
        this.init_capcha()
    },
    methods:{
        reset(){
            this.name='',this.email='',this.message=''
        },
        init_capcha(){
            init_capcha(this);
        },
        
        check_form(){
            clear_errors(this);
            return check_form(this)

        },
        submit(){
            let exists_errors=this.check_form();
            if(!exists_errors){
                axios.post(
                    '/consultation',{
                        action:'form_send',
                        name:this.name,
                        phone: this.phone,
                        email: this.email,
                        message: this.message,
                        dat: this.dat,
                        capture_key:this.form_capture_key,
                        capture_str:this.form_capture_str
                    }
                ).then(
                    (r)=>{
                        let d=r.data;
                        if(d.success){
                            $('#modal_thanks').jmodal('show');
                            this.reset()
                        }
                        else{
                            for(let e of d.errors){
                                if(e=='capture_str')
                                    this.error.form_capture_str='проверочный ключ заполнен неверно'
                                else
                                    this.error[e]='поле не заполнено или заполнено неверно'
                            }
                        }
                    }

                )
            }
        }
    }
})