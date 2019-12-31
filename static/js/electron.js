const { app, BrowserWindow, Menu } = require('electron');
const url = require('url');
const path = require('path');
const pyshell = require('python-shell')
const child = require('child_process').execFile;
const fs = require('fs')

var pathApp = 'app.py';
var pathProcess = 'process.py'

let window

/* child(pathApp, () => {
  console.log('Running')
}) */

pyshell.run(pathApp, () => {
  console.log('Running...')
});

function createWindow() {

  window = new BrowserWindow({
    width: 800,
    height: 650,
    resizable: false,
    icon: 'static/images/partner.ico',
    fullscreen: false,
  })

  // window.loadURL('http://localhost:5000/')

  window.loadFile('templates/load.html')

  const mainMenu = Menu.buildFromTemplate(menuTemplate)
  Menu.setApplicationMenu(mainMenu)

};

app.on('ready', () => {
  setTimeout(createWindow, 7000);
})

// Antes de quitar la aplicación este codigo ejecuta lo que esta dentro de la función flecha

app.on('window-all-closed', () => {
  if (process.platform != 'darwin') {
    /* child(pathProcess, () => {
      app.quit()
    }) */
    pyshell.run(pathProcess, () => {
      app.quit()
    })
  }
})

const menuTemplate = [
  {
    label: 'Archivo',
    submenu: [
      {
        label: 'Buscar Socio',
        accelerator: 'Ctrl+S',
        click() {
          function Search() {
            window.loadURL('http://localhost:5000/search')
          };
          Search();
        }
      },
      {
        label: 'Registrar Socio',
        accelerator: 'Ctrl+N',
        click() {
          function partnerRegister() {
            window.loadURL('http://localhost:5000/register')
          };
          partnerRegister();
        }
      },
      {
        label: 'Listar Socios',
        accelerator: 'Ctrl+L',
        click() {
          window.loadURL('http://localhost:5000/socios/1')
        }
      },
      {
        label: 'Salir del programa',
        accelerator: 'Ctrl+Shift+Q',
        click() {
          /* child(pathProcess, () => {
            console.log('Running');
            if (process.platform != 'darwin') {
              app.quit()
            }
          }); */
          pyshell.run(pathProcess, () => {
            if (process.platform != 'darwin') {
              app.quit()
            }
          } )
        }
      }
    ]
  },
  {
    label: 'Ver',
    submenu: [
      {
        label: 'Actualizar Página',
        accelerator: 'Ctrl+R',
        click() {
          window.reload()
        }
      },
      {
        label: 'Developer Tools',
        accelerator: 'Ctrl+Shift+I',
        click() {
          window.toggleDevTools();
        }
      }
    ]
  }
]











