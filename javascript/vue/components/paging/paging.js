Vue.component(
  'paging',{
    props:['total_count','page', 'go_search','perpage','visible_count'],
    data(){
      return {
        end_page:0, // последняя выводимая страница
        start_page:0, // первая выводимая страница
        maximum_page: '' // максимальная страница (не стал называть max_page, чтобы можно было max_page передать в параметрах)
      }
    },
    created(){
      this.page=parseInt(this.page)
      if(!this.visible_count)
        this.visible_count=5
    },
    methods:{

    },

    computed:{
      max_page(){

      },
      list(){
        let list=[]
        let startpage=parseInt(this.page - parseInt(this.visible_count/2))
        if(startpage<0) startpage=0
        this.startpage=startpage
        let end_page=startpage+parseInt(this.visible_count)
        
        let max_page=Math.ceil(this.total_count/this.perpage)

        this.maximum_page=max_page
        console.log('startpage:',startpage)
        console.log('end_page:'+end_page)
        console.log('max_page:'+max_page)
        let cur_page=startpage;
        while(cur_page<max_page && (cur_page < end_page) ){
          
          list.push(cur_page)
          this.max_out_page=cur_page
          cur_page++
        }
        return list
      }
    },
  template:`
    <div>
      <nav>
        <ul class="pagination pagination-sm">
          <li class="page-item" v-if="page>0"><a class="page-link" href="#" @click.prevent="go_search(0)">В начало</a></li>
          <li class="page-item" v-if="page>0"><a class="page-link" href="#" @click.prevent="go_search(page-1)">&lt;</a></li>
          <li class="page-item" v-for="p in list" :class="{'active':(p==page)}"><a class="page-link" href="#" @click.prevent="go_search(p)">{{p+1}}</a></li>
          <li class="page-item" v-if="page<maximum_page"><a class="page-link" href="#" @click.prevent="go_search(p+1)">&gt;</a></li>
          <li class="page-item" v-if="page<maximum_page"><a class="page-link" href="#" @click.prevent="go_search(maximum_page-1)">В конец</a></li>
        </ul>
      </nav>
    </div>

  `

  },


);