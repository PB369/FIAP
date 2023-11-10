import './css/Footer.scss'

const Footer = () => {

  const listMedias = [
    {
      name: "linkedin",
      path: "../../../imagens/linkedin.png",
      link: "#"
    },
    {
      name: "instagram",
      path: "../../../imagens/instagram.png",
      link: "#"
    },
    {
      name: "whatsapp",
      path: "../../../imagens/whatsapp.png",
      link: "#"
    }
  ]

  const medias = listMedias.map(media =>
    <li key={media.name} className='me-2'>
      <a href={media.link} target={"_self"} rel="noreferrer">
        <img 
        src={media.path}
        draggable="false"/>
      </a>
    </li>)

  return (
    <footer className='row d-flex justify-content-between align-items-center py-4 px-0 mx-0 container-fluid'>
      <div className='footerElements flex-column d-flex justify-content-center align-items-center px-0 col-md-4'>
        <img src='../../../imagens/logo.png' draggable="false"/>
        <p className='mt-3 mb-0 px-0 text-center'>Comic Store 2023</p>
      </div>
      <div className='footerElements flex-column d-flex justify-content-center align-items-center px-0 text-center col-md-4'>
        <p className='my-0'>RM97937 - Pedro Barros</p>
        <p className='my-0'>&copy; Todos os direitos reservados.</p>
      </div>
      <div className='footerElements px-0 col-md-4'>
        <ul className='d-flex flex-row my-3 justify-content-center align-items-center px-0'>
          {medias}
        </ul>
      </div>
    </footer>
  )
}

export default Footer