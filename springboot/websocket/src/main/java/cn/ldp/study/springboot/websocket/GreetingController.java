package cn.ldp.study.springboot.websocket;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.handler.annotation.SendTo;
import org.springframework.messaging.simp.SimpMessagingTemplate;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class GreetingController {

    @Autowired
    private SimpMessagingTemplate messagingTemplate;


    //接收/app/hello发来的value，然后将方法返回值，转发到/topic/greetings客户端
    @MessageMapping("/hello")
    @SendTo("/topic/greetings")
    public Greeting greeting(HelloMessage message) throws Exception {
        Thread.sleep(1000);
        return new Greeting("Hello, " + message.getName() + "!");
    }

    @MessageMapping("/message")
    public Greeting message(String message) throws Exception{
        //通过convertAndSendToUser 向用户发送信息,
        // 第一个参数是接收消息的用户,第二个参数是浏览器订阅的地址,第三个参数是消息本身
//        messagingTemplate.convertAndSendToUser();

        messagingTemplate.convertAndSend("/topic/greetings",new Greeting(message));
        return null;
    }
}