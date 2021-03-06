function close_on_escape(self){
    addEventListener('keydown',
      function(e){ 
        if(e.key=='Escape' && self.list.length){
          self.ajax_attempt='esc'
          self.show_list=false
          if(self.click_listener){
            document.removeEventListener('click', self.click_listener,false)
          }
        }
      }
    )
}

function click_out_init(self){ // вешаем событие на клик снаружи
    
    self.click_listener=function(e) {
        let list = document.querySelector('#'+self.id);
        if(!list || !self.show_list){
          document.removeEventListener('click', self.click_listener,false)
          return 
        }
        const target=e.target
        self.show_list=(target == list || list.contains(target));
        if(!self.show_list){
          document.removeEventListener('click', self.click_listener,false)
        }
    }
    
    setTimeout(
            ()=>{
              self.click_listener=document.addEventListener('click', self.click_listener,false)
            },
            500
    )

}

Vue.component('autocomplete-place', {
  props:{
    updater:Function,
    value: Object,
    placeholder: String,
    multi: Boolean,
    ajax_action:{
      required: true,
      type: String
    },
    only_text:{
      Boolean
    }
  },
  model:{
    prop:'value',
    event:'input'
  },
  created(){
    this.id='autocomplete'+parseInt(Math.random()*200000);
    click_out_init(this)
    close_on_escape(this)
  },
  methods:{
    update_v_model(){

      let values=[]
      for(let l of this.setter_value)
        values.push(l.value)
      if(this.updater){ // Функция, которая ловит изменения
        this.updater(values)
      }
      else{
        this.$emit('input', values)
      }
      
    },
    go_ajax(){
      
      axios.get(
        this.ajax_action+( (this.ajax_action.indexOf('?')>-1)?'&':'?')+'term='+this.in_value
      ).then(
        r=>{
          let d=r.data
          if(d.success){
            this.list=d.list
            for(let l of d.list){
              d.on=false
            }

            this.show_list=true
            click_out_init(this)
          }
        }
      )
    },
    change(e){
      if(this.ajax_attempt=='esc'){
        this.ajax_attempt=0
        return
      }
      if(this.in_value.length>=3){
        this.ajax_attempt++
        setTimeout(
          ()=>{
            if(this.ajax_attempt=='esc')
              this.ajax_attempt=0
            else
              this.ajax_attempt--
            if(!this.ajax_attempt)
              this.go_ajax()
          }
        )
      }
    },
    remove_value(cur){
      this.exists[cur.value]=false
      let new_value_list=[]
      
      for(let v of this.setter_value){
        if( v.value != cur.value){
          new_value_list.push(v)
        }
      }
      this.setter_value=new_value_list
      this.update_v_model()
    },
    select(cur){
      if(this.multi){
        if(cur.on){
          this.setter_value.push(cur)
          this.exists[cur.value]=true
          
        }
        else{
          this.remove_value(cur)
        }

      }
      else{

        if(this.only_text)
          this.setter_value=[cur.header]
        else
          this.setter_value=[cur.value]

        this.in_value=cur.header

        
        
      }
      this.update_v_model()


      
      
      

    }

    
  },
  computed:{


  },
  data: function () {
    
    return {
      exists:{}, // уже выбранные значения
      click_listener:false,
      ajax_attempt:0,
      id:'',
      in_value:'',
      setter_value:[],
      //setter_headers:['регион1','регион2','регион3','регион4'],
      show_list:false,
      list:[]
    }
  },
  template: `
    <div>
      <pre v-if="0">{{setter_value}}</pre> 
      
      <input type="text" class="form-control" v-model="in_value"  :placeholder="placeholder" @keyup="change()" autocomplete="new-password">
      <div class="popup_ac" v-if="show_list" :id="id">
        
        <template v-if="multi">
          <div v-for="l in list" value="l.value" ><input type="checkbox" @change="select(l)" v-model="l.on"> {{l.header}}</div>
        </template>
        <template v-else>
          <div v-for="l in list" value="l.value" @click="select(l)">{{l.header}}</div>
        </template>
      </div>
      <div v-if="multi">
            <div v-for="l in setter_value">{{l.header}} <a href="" @click.prevent="remove_value(l)">удалить</a></div>
      </div>
  `
})
