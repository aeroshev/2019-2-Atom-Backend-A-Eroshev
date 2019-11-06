const template = document.createElement('template');
template.innerHTML = `
<style>
  *{
    box-sizing: border-box;
  }
  li{
    list-style: none;
  }
  :host{
    width: 100%;
    height: 100%;
    background-color: #373338;
    background-size: 50px;
    display: flex;
    flex-direction: column;
  }
  .header{
    position: absolute;
    left: 0; top: 0;
    background-color: #8E24AA;
    width: 100%;
    z-index: 1;
  }

  ::-webkit-scrollbar {
    width: 0px;
  }
  .messageWrap{
    margin-top: 60px;
    margin-bottom: 50px;
    height: 100%;
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    align-content: flex-start;
    overflow: hidden;
    overflow-y: scroll;  
  }
  message-box{
    box-sizing: border-box;
    /*overflow: hidden;*/
    width: 100%;
    padding: 0 4px 0 4px;
    animation-name: smoothDrop;
    animation-duration: 0.5s;
    animation-timing-function: ease-in-out;
    animation-fill-mode: forwards;
  }
  @keyframes smoothDrop {
    from {
        transform: translate(-100%) scaleX(0)
    }
    to {
        transform: translate(0) scaleX(1)
    }
  }
  .footer{
    position: absolute;
    left: 0; 
    bottom: 0;
    width: 100%;
    background-color: #f8fff9;
    outline: 1px solid rgba(5,0,0,0.94);
    z-index: 1;
  }
</style>
<div class="header">
    <dialog-info></dialog-info>
</div>
<div class="messageWrap"></div>
<div class="footer">
  <form-input placeholder="Message" name="scroll"></form-input>
</div>
`;

class MessageForm extends HTMLElement {
  constructor() {
    super();

    this.shadowRoot = this.attachShadow({ mode: 'open' });
    this.shadowRoot.appendChild(template.content.cloneNode(true));

    this.$input = this.shadowRoot.querySelector('form-input');
    this.$messages = this.shadowRoot.querySelector('.messageWrap');
    this.$toolBar = this.shadowRoot.querySelector('dialog-info');

    this.$input.addEventListener('onSubmit', this.onSubmit.bind(this));

    this.lastMessage = undefined;
    this.timeSend = undefined;
    this.dialogID = undefined;
  }

  // при обновлении страницы эта функция выгружает из localStorage историю сообщений
  messageLoader(dialogID) {
    const json = localStorage.getItem(`dialogID_${dialogID}`);

    let messageArray = 0;
    try {
      messageArray = JSON.parse(json);
    } catch (SyntaxError) {
      localStorage.clear();
    }
    if (messageArray != null) {
      for (let index = 0; index < messageArray.length; index++) {
        this.renderMessage(messageArray[index]);
      }
    }
  }

  clearChat() {
    this.$messages.innerHTML = '';
  }

  setId(dialogID) {
    this.dialogID = dialogID;
  }

  getLast() {
    let messageList = [];
    const json = localStorage.getItem(`dialogID_${this.dialogID}`);
    try {
      messageList = JSON.parse(json);
    } catch (SyntaxError) {
      alert("Can't unpacked storage");
    }
    if (messageList != null) {
      const lastMessageBox = messageList[messageList.length - 1];
      this.lastMessage = lastMessageBox.message;
      this.timeSend = lastMessageBox.time;
    } else {
      this.lastMessage = '';
      this.timeSend = 0;
    }
  }

  countUnreadMessage() {
    let messageList = [];
    const json = localStorage.getItem(`dialogID_${this.dialogID}`);
    try {
      messageList = JSON.parse(json);
    } catch (SyntaxError) {
      alert("Can't unpacked storage");
    }

    let quantityUnreadMessages = 0;
    if (messageList != null) {
      for (let index = 0; index < messageList.length; index++) {
        if (messageList[index].read === 'unread') {
          quantityUnreadMessages++;
        }
      }
    }
    return quantityUnreadMessages;
  }

  /*
  // рендеринг объекта времени
  renderDate(time) {
    let elem = document.createElement('date-marker');
    elem = this.$messages.appendChild(elem);
    elem.setAttribute('time', time);
  }
*/
  // рендеринг объекта сообщения
  renderMessage(messageBox) {
    /* this.renderDate(messageBox.time); */

    let elem = document.createElement('message-box');
    elem = this.$messages.appendChild(elem);

    elem.setAttribute('messageID', messageBox.messageID);
    elem.setAttribute('owner', messageBox.owner);
    elem.setAttribute('text', messageBox.message);
    elem.setAttribute('time', messageBox.time);
  }

  // создание новго сообщения
  newMessage(owner, text, additions = null) {
    // полуаем текущее время
    const time = new Date();
    // задаём атрибуты messageBox
    const messageBox = {
      messageID: this.dialogID + localStorage.length,
      owner: ((owner) ? 'opposite' : 'self'),
      message: text,
      additions,
      time: time.getTime(),
      read: 'read',
    };

    this.lastMessage = messageBox.message;
    this.timeSend = messageBox.time;

    // сохраняем в localStorage в виде JSON
    let messageArray = JSON.parse(localStorage.getItem(`dialogID_${this.dialogID}`));
    if (messageArray === null) {
      messageArray = [];
    }
    messageArray.push(messageBox);

    localStorage.setItem(`dialogID_${this.dialogID}`, JSON.stringify(messageArray));
    this.renderMessage(messageBox);
  }

  onSubmit() {
    if (this.$input.value !== '') {
      this.newMessage(0, this.$input.value);
      // очистка поля ввода
      this.$input.setAttribute('value', '');
    }
  }
}

customElements.define('message-form', MessageForm);
