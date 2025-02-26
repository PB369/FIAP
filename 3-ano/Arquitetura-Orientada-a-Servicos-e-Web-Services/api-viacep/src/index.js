const express = require('express')
const axios = require('axios')

const app = express()
const PORT = 3000

app.get('/cep/:cep', async(req, res) => {
    const {cep} = req.params

    try {
        const response = await axios.get(`https://viacep.com.br/ws/${cep}/json`)
        const endereco = response.data

        if(endereco.erro) {
            return res.status(404).json({mensagem: 'CEP não encontrado'})
        }

        res.json({
            cep: endereco.cep,
            logradouro: endereco.logradouro,
            bairro: endereco.bairro,
            cidade: endereco.localidade,
            estado: endereco.uf
        })
    } catch(erro) {
        res.status(500).json({mensagem: 'Erro ao consultar o CEP'})
    }
})

app.listen(PORT, () => {
    console.log(`Servidor rodando em http://localhost:${PORT}`)
})