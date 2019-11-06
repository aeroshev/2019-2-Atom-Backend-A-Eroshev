const template = document.createElement('template');
template.innerHTML = `
<style>

 message-form {
    position: absolute;
    display: none;
    /*overflow: hidden;*/
    z-index: 1;
    animation-name: smoothOpen;
    animation-duration: 0.5s;
    animation-timing-function: ease-in-out;
    animation-fill-mode: forwards;
 }
 
  @keyframes smoothOpen {
    from {
        transform: translate(-100%) scaleX(0)
    }

    to {
        transform: translate(0) scaleX(1)
    }
}

 dialog-list {
    position: absolute;
    overflow: visible;
    z-index: 1;
    animation-name: smoothClose;
    animation-duration: 0.5s;
    animation-timing-function: ease-in-out;
    animation-fill-mode: forwards;
 }
   @keyframes smoothClose {
    from {
        transform: translate(-100%) scaleX(0)
    }

    to {
        transform: translate(0) scaleX(1)
    }

}
</style>
<dialog-list></dialog-list>
<message-form></message-form>
`;

class GetDialog extends HTMLElement {
  constructor() {
    super();

    this.shadowRoot = this.attachShadow({ mode: 'open' });
    this.shadowRoot.appendChild(template.content.cloneNode(true));

    this.$dialogList = this.shadowRoot.querySelector('dialog-list');
    this.$chatForm = this.shadowRoot.querySelector('message-form');

    this.shadowRoot.addEventListener('addNewChat', () => this.addListenerOpenDialog());
    this.collectorListener = undefined;
    this.openedChatId = undefined;

    this.addListenerOpenDialog();
  }

  addListenerOpenDialog() {
    if (this.collectorListener === undefined) { this.collectorListener = []; }

    let dialogList = [];
    const json = localStorage.getItem('dialogList');
    try {
      dialogList = JSON.parse(json);
    } catch (SyntaxError) {
      alert("Can't unpacked storage");
    }

    dialogList.forEach((dialogID) => {
      if (!(dialogID in this.collectorListener)) {
        const elem = this.$dialogList.$content.querySelector(`dialog-box[dialogid="${dialogID}"]`);
        elem.addEventListener('click', () => this.openChat(dialogID));
        this.collectorListener.push(dialogID);
      }
    });
  }

  openChat(dialogID) {
    this.openedChatId = dialogID;

    this.$chatForm.style.display = 'flex';
    this.$dialogList.style.display = 'none';

    this.$chatForm.clearChat();
    this.$chatForm.setId(dialogID);
    this.$chatForm.messageLoader(dialogID);

    this.$chatForm.$toolBar.addEventListener('pressExit', () => this.closeChat());
    this.$chatForm.$toolBar.addEventListener('clickBackButton', () => this.closeChat());
  }

  closeChat() {
    this.$chatForm.style.display = 'none';
    this.$dialogList.style.display = 'flex';

    this.UpdateList(this.openedChatId);
  }

  UpdateList(openedChatId) {
    const elem = this.$dialogList.$content.querySelector(`dialog-box[dialogid="${openedChatId}"]`);
    if (this.$chatForm.lastMessage && this.$chatForm.timeSend) {
      this.$chatForm.getLast();
      if (this.$chatForm.lastMessage !== '' && this.$chatForm.timeSend !== 0) {
        elem.setAttribute('lastmessage', this.$chatForm.lastMessage);
        elem.setAttribute('timelastmessage', this.$chatForm.timeSend);
        elem.setAttribute('messagestatus', this.$chatForm.countUnreadMessage());
      }
    }
  }
}

customElements.define('get-dialog', GetDialog);
