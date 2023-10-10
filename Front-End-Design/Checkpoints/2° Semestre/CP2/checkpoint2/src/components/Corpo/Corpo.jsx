import './css/main.css'

const Corpo = () => {
  return(
      <main>
        <h3>Conheça nossos sabores!</h3>
        <div className='pizzas'>
          <h4>Atum & Cebola</h4>
          <img src="../../pizza1.jpg"></img>
          <div id="info-pizza">
            <p><span>Ingredientes</span>: Queijo, Atum e Cebola</p>
            <p><span>Preço:</span> R$55,00</p>
          </div>
        </div>
        <div className='pizzas'>
          <h4>Tradicional Calabresa</h4>
          <img src="../../pizza2.jpg"></img>
          <div id="info-pizza">
            <p><span>Ingredientes</span>: Queijo, Calabresa e Cebola</p>
            <p><span>Preço:</span> R$45,00</p>
          </div>
        </div>
        <div className='pizzas'>
          <h4>Calabresa Plus</h4>
          <img src="../../pizza3.jpg"></img>
          <div id="info-pizza">
            <p><span>Ingredientes</span>: Queijo, Calabresa, Cebola, Milho e Azeitona Preta</p>
            <p><span>Preço:</span> R$58,00</p>
          </div>
        </div>
        <div className='pizzas'>
          <h4>Pizza Mussarela</h4>
          <img src="../../pizza4.jpg"></img>
          <div id="info-pizza">
            <p><span>Ingredientes</span>: Queijo, Tomate e Azeitona Preta</p>
            <p><span>Preço:</span> R$38,00</p>
          </div>
        </div>
        <div className='pizzas'>
          <h4>Napolitana</h4>
          <img src="../../pizza5.webp"></img>
          <div id="info-pizza">
            <p><span>Ingredientes</span>: 4 Queijos, Tomate e Azeitona Preta</p>
            <p><span>Preço:</span> R$35,00</p>
          </div>
        </div>
        <div className='pizzas'>
          <h4>Brócolis</h4>
          <img src="../../pizza6.jpg"></img>
          <div id="info-pizza">
            <p><span>Ingredientes</span>: Queijo, Brócolis e Catupiry</p>
            <p><span>Preço:</span> R$50,00</p>
          </div>
        </div>
      </main>
      )
}

export default Corpo