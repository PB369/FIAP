import styled from 'styled-components'

export const Header = styled.header`
  background-color: lightsalmon;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  padding: 30px;
  margin-bottom: 15px;
  box-shadow: 0 3px 5px rgba(0, 0, 0, 0.3);

  h1 {
    margin-bottom: 5px;
  }

  h2 {
    font-style: italic;
  }
`

export const Footer = styled.footer`
  background-color: lightsalmon;
  padding: 20px;
  text-align: center;
  box-shadow: 0 -3px 5px rgba(0, 0, 0, 0.3);
  margin-top: 25px;

  p {
    font-weight: bold;
  }
  
`