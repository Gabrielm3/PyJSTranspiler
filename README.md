<h1>PyJSTranspiler</h1>
<p>O PyJSTranspiler é uma ferramenta que permite transpilar Python em JavaScript.</p>

<div>
    <img src="https://github.com/Gabrielm3/PyJSTranspiler/blob/master/PyJSTranspiler.png" alt="Go">
</div>

<h2>Como usar</h2>
<p>Para usar o PyJSTranspiler, basta seguir as etapas abaixo:</p>

<ol>
  <li>Instale o Python no seu sistema</li>
  <li>Verifique se o Python foi instalado com o comando: <code>python --version</code></li>
  <li>Clone o repositório do PyJSTranspiler: <code>git clone https://github.com/gabrielm3/pyjstranspiler.git</code></li>
  <li>Navegue para a pasta raiz do repositório: <code>cd PyJSTranspiler</code></li>
  <li>Execute o seguinte comando para gerar o código JavaScript transpilado: <code>python indentedCode.py</code></li>
  <li>O código JavaScript transpilado será gravado no arquivo <code>output.js</code></li>
</ol>

<h2>Exemplo de uso</h2>
<p>Aqui está um exemplo de código Python que pode ser transpilado para JavaScript usando o PyJSTranspiler:</p>

<pre><code>def greet(name):
    print(f"Hello, {name}!")

names = ["Gabriel", "Ana", "Fernanda", "Alice"]

for name in names:
    greet(name)
</code></pre>

<p>O código JavaScript transpilado será o seguinte:</p>

<pre><code>function greet(name) {
    console.log(`Hello, ${name}!`);
}

let names = ["Gabriel", "Ana", "Fernanda", "Alice"];

for (let name of names) {
    greet(name);
}
</code></pre>

<h2>Contribuição</h2>
<p>Se você deseja contribuir para o projeto PyJSTranspiler, sinta-se à vontade para criar um fork do repositório e enviar pull requests com novas funcionalidades ou correções de bugs.</p>
