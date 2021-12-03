var ws = null;
//if(window.outerWidth < 1024){ // моб. устройство

//}
var app

const init_sizes=()=>{
    

    //document.getElementById('app').style.height=window.innerHeight+'px'
    let height_form=document.getElementById('sendform').clientHeight
    let height_header=document.querySelector('.header').clientHeight
    let mes_height=(window.innerHeight-height_form-height_header-70)
    console.log(
        `
            height_form: ${height_form}
            height_header: ${height_header}
            message_window: ${window.innerHeight} - ${height_form} - ${height_header} = ${mes_height}px
        `
    )
    
    
    //document.getElementById('message_window').style.height=(document.getElementById('message_window').clientHeight-height_form-height_header)+'px'
    document.getElementById('message_window').style.height=mes_height+'px'
    console.log(document.getElementById('message_window').clientHeight)

}
window.onresize=(
    ()=>{
        init_sizes()
    }
)

app=new Vue({
    el: '#app',
    data:{
        client_id:client_id,
        token: 'some-key-token'+client_id,
        profile: {},
        names_hash:{},
        list_messages:[],
        messageText:''
    },
    created(){
        document.title=`Чат ${client_id}`
        this.connect()
        this.getMessages()
    },
    methods:{
        scrollEnd(){
            this.$nextTick(
                ()=>{
                    let sw=document.getElementById('message_window')
                    sw.scrollTop=sw.scrollHeight
                }
            )
        },
        connect(event){
            
            
            //ws = new WebSocket("ws://localhost:5000/ws/" + this.client_id + "/ws?token=" + this.token);
            ws = new WebSocket("ws://localhost:5000/ws/" + this.client_id)
            
            ws.onmessage = event => {
                if(event){
                    this.list_messages.push(JSON.parse(event.data))
                    this.scrollEnd()
                    document.querySelector('#messageText').focus()
                }

            };
            //event.preventDefault()
        },
        getMessages(){
            axios.get(
                `/init/${client_id}`
            ).then(
                r=>{
                    let d=r.data
                    this.list_messages=d.messages
                    this.profile=d.profile
                    this.names_hash=d.names_hash
                    // прокручиваем в самый низ scroll
                    this.$nextTick(
                        ()=>{

                            init_sizes()
                            this.scrollEnd()
                            document.querySelector('#messageText').focus()
                        }
                    )
                }
            )
        },
        sendMessage(event){
            console.log('event:',event)
            let message=this.messageText.trim()
            if(message){
                ws.send(message)
                this.messageText=''
            }

        },
        itsMe(message){
            return (message.client_id==this.profile.id)
        },
        nameColor(message){
            return '#35cd96'
        }
    }
})

const ctrl_enter_press=(e)=>{
        console.log('keydown')
        if (e.ctrlKey && ((event.keyCode == 0xA)||(event.keyCode == 0xD)) ) {
            
            console.log('ctrl+enter')
            app.sendMessage(e)
        }
    }

