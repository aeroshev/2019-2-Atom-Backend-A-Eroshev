const template = document.createElement('template');
template.innerHTML = `
<style>
  *{
    box-sizing: border-box;
  }
  :host{
    height: 60px;
    display: flex;
    flex-direction: row;
  }
  .headerButton{
    height: 100%;
    /*width: 120px;*/
    /*margin: 0 5px;*/
    cursor: pointer;
  }
  .statusConteiner{
    flex: auto;
    height: 100%;
    padding: 5px 0;
    width: 50%;
    display: flex;
    flex-direction: row;
    justify-content: center;
  }
  .statusConteiner .userAvatar{
    height: 100%;
    width: 50px;
    border-radius: 30px;
    margin-right: 10px;
    margin-left: 10px;
    background: url(https://cdn.iconscout.com/icon/free/png-256/avatar-367-456319.png) no-repeat center center;
    background-size: 100%; 
  }
  
  .statusConteiner .userName{
    height: 100%;
    padding-top: 5px;
  }
  .userName .name{
    font-size: medium;
    color: #fbfbff;
  }
  .userName .status{
    font-size: medium;
    color: #fbfbff;
  }

  .headerButton .backButton{
    background-size: 100%;
    width: 40px;
    height: 40px;
    margin: 10px;
    background: url(https://cdn2.iconfinder.com/data/icons/simple-circular-icons-line/84/Left_Carrot-512.png) no-repeat center center;
    background-size: 100%;
  }
  
  .headerButton .searchButton{
    background-size: 100%;
    display: inline-block;
    height: 100%;
    width: 40px;
    float: left;
    background: url(https://static.thenounproject.com/png/424968-200.png) no-repeat center center;
    background-size: 70%;
  }
  
  .headerButton .optionsButton{
    background-size: 100%;
    display: inline-block;
    height: 100%;
    width: 50px;
    background: url(https://static.thenounproject.com/png/703781-200.png) no-repeat center center;
    background-size: 100%;
  }

</style>
<div class="headerButton">
    <div class="backButton"></div>
</div>
<div class="statusConteiner">
    <div class="userAvatar"></div>
        <div class="userName">
        <div class="name">Eroshev Artem</div>
        <div class="status">в сети</div>
    </div>
</div>
<div class="headerButton">
    <div class="searchButton"></div>
    <div class="optionsButton"></div>
</div>
`;

class DialogInformation extends HTMLElement {
  constructor() {
    super();

    this.shadowRoot = this.attachShadow({ mode: 'open' });
    this.shadowRoot.appendChild(template.content.cloneNode(true));

    this.$backButton = this.shadowRoot.querySelector('.backButton');
    this.$searchButton = this.shadowRoot.querySelector('.searchButton');
    this.$optionsButton = this.shadowRoot.querySelector('.optionsButton');

    this.$backButton.addEventListener('keypress', this.escPress.bind(this));
    this.$backButton.addEventListener('click', this.backButton.bind(this));
    this.$searchButton.addEventListener('click', this.searchButton.bind(this));
  }

  escPress(event) {
    if (event.keyCode === 27) this.escape();
  }

  escape() {
    this.dispatchEvent(new Event('pressExit'));
  }

  backButton() {
    this.dispatchEvent(new Event('clickBackButton'));
  }

  searchButton() {
    this.dispatchEvent(new Event('clickSearchButton'));
  }
}

customElements.define('dialog-info', DialogInformation);
