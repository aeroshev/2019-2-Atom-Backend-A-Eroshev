const template = document.createElement('template');
template.innerHTML = `
<style>
  * {
    box-sizing: border-box;
  }
  li {
    list-style: none;
  }
  .dialogWrap {
    width: 100%;
    height: 90px;
    display: inline-block;
    text-align: center;
    word-break: break-all;
    float: left;
    color: black;
  }
  
  .dialogWrap .dialogName {
    width: 50%;
    height: 20px;
    padding-left: 20%;
    text-align: left;
    font-size: small;
  }
  
  .dialogWrap .dialogAvatar {
    display: inline-block;
    float: left;
    width: 60px;
    height: 60px;
    margin: 0px;
    border-radius: 30px;
    background: url(https://cdn.iconscout.com/icon/free/png-256/avatar-367-456319.png) no-repeat center center;
    background-size: 100%;
  }
  
  .dialogWrap .messageTime {
    width: 60px;
    height: 20px;
    text-align: right;
    font-size: small;
    margin-top: 5px;
    margin-bottom: 5px;
    float: right;
  }
  
  .dialogWrap .lastMessage {
    width: 100%;
    height: 40px;
    padding-left: 100px;
    padding-right: 60px;
    text-align: left;
  }
  
  .dialogWrap .messageStatus {
    float: right;
  }

</style>
<li>
    <div class="dialogWrap">
        <div class="dialogName"></div>
        <div class="dialogAvatar"></div>
        <div class="messageTime"></div>
        <div class="lastMessage"></div>
        <div class="messageStatus"></div>
    </div>
</li>
`;

class DialogBox extends HTMLElement {
  constructor() {
    super();

    this.shadowRoot = this.attachShadow({ mode: 'open' });
    this.shadowRoot.appendChild(template.content.cloneNode(true));

    this.$dialogName = this.shadowRoot.querySelector('.dialogName');
    this.$userAvatar = this.shadowRoot.querySelector('.dialogAvatar');
    this.$messageTime = this.shadowRoot.querySelector('.messageTime');
    this.$lastMessage = this.shadowRoot.querySelector('.lastMessage');
    this.$messageStatus = this.shadowRoot.querySelector('.messageStatus');
  }

  static get observedAttributes() {
    return ['dialogname', 'lastmessage', 'timelastmessage', 'messagestatus'];
  }

  attributeChangedCallback(name, oldValue, newValue) {
    switch (name) {
      case 'dialogname':
        this.$dialogName.innerText = newValue;
        break;

      case 'lastmessage':
        this.$lastMessage.innerText = newValue;
        break;

      case 'timelastmessage':
        let date = new Date(parseInt(newValue, 10));
        date = date.toString().split(' ')[4].split(':');
        this.$messageTime.innerText = date[0] + ':' + date[1];
        break;

      case 'messagestatus':
        this.$messageStatus.innerText = newValue;
        break;
    }
  }
}

customElements.define('dialog-box', DialogBox);
