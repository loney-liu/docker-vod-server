function MyAwesomePanel(viewer, container, id, title, options) {
    this.viewer = viewer;
    Autodesk.Viewing.UI.DockingPanel.call(this, container, id, title, options);

    // the style of the docking panel
    // use this built-in style to support Themes on Viewer 4+
    this.container.classList.add('docking-panel-container-solid-color-a');
    this.container.style.top = "10px";
    this.container.style.left = "10px";
    this.container.style.bottom = "10px";
    this.container.style.width = "auto";
    this.container.style.height = "auto";
    this.container.style.resize = "auto";


    var token = login(sg_shot_url, sg_script, sg_key, this.container)
    
    // and may also append child elements...

}
MyAwesomePanel.prototype = Object.create(Autodesk.Viewing.UI.DockingPanel.prototype);
MyAwesomePanel.prototype.constructor = MyAwesomePanel;

class MyAwesomeExtension extends Autodesk.Viewing.Extension {
    constructor(viewer, options) {
        super(viewer, options);
        this._group = null;
        this._button = null;
    }

    load() {
        console.log('MyAwesomeExtensions has been loaded');
        return true;
    }

    unload() {
        // Clean our UI elements if we added any
        if (this._group) {
            this._group.removeControl(this._button);
            if (this._group.getNumberOfControls() === 0) {
                this.viewer.toolbar.removeControl(this._group);
            }
        }
        console.log('MyAwesomeExtensions has been unloaded');
        return true;
    }

    onToolbarCreated() {
        // Create a new toolbar group if it doesn't exist
        this._group = this.viewer.toolbar.getControl('allMyAwesomeExtensionsToolbar');
        if (!this._group) {
            this._group = new Autodesk.Viewing.UI.ControlGroup('allMyAwesomeExtensionsToolbar');
            this.viewer.toolbar.addControl(this._group);
        }

        // Add a new button to the toolbar group
        this._button = new Autodesk.Viewing.UI.Button('myAwesomeExtensionButton');
        this._button.onClick = (ev) => {
            console.log("my awsome button clicked")
            // Check if the panel is created or not
            if (this._panel == null) {
                this._panel = new MyAwesomePanel(this.viewer, this.viewer.container, 'modelSummaryPanel', 'Snapshots');
            }
            // Show/hide docking panel
            this._panel.setVisible(!this._panel.isVisible());

            // If panel is NOT visible, exit the function
            if (!this._panel.isVisible())
                return;
        };
        this._button.setToolTip('Review Snapshots');
        this._button.addClass('myAwesomeExtensionIcon');
        this._group.addControl(this._button);
    }
}


class ModelSummaryPanel extends Autodesk.Viewing.UI.PropertyPanel {
    constructor(viewer, container, id, title, options) {
        super(container, id, title, options);
        this.viewer = viewer;
    }
}


Autodesk.Viewing.theExtensionManager.registerExtension('MyAwesomeExtension', MyAwesomeExtension);

function login(host, username, password, mycontainer) {
    var headers = {
        'Accept':'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    $.ajax({
        url: host + '/api/v1/auth/access_token',
        method: 'post',
        headers: headers,
        data: {
            'grant_type': 'client_credentials',
            'client_id': username,
            'client_secret': password
        },
        success: function(data) {
            console.log(JSON.stringify(data))
            var access_token = data.access_token
                    
            //list_projects(host, access_token)
            // this is where we should place the content of our panel
            get_notes(host, access_token, mycontainer)
        },
        error: function(data) {
            alert('Auth Failed.');
        }
    });
    return false;
}

function get_notes(host, access_token, mycontainer){
    var forge_urn = document.getElementById("forge_urn").value

    var request_headers = {
        'Content-Type':'application/vnd+shotgun.api3_array+json',
        'Accept':'application/json',
        'Authorization': 'Bearer ' + access_token
    }
    data = { 
        "filters": [ 
            ["note_links.Asset.sg_forge_urn", "is", forge_urn] 
        ] 
    };
    $.ajax({
        url: host + '/api/v1/entity/notes/_search/?fields=id,content',
        method: 'post',
        headers: request_headers,
        data: JSON.stringify(data),
        success: function(data) {
            img_list = ""
            count = 1
            data["data"].forEach(element => {
                img_item = " <img height='200px' width='200px' src='"+element["attributes"]["content"]+ "'</img> "
                if(count%3 == 0){
                    img_list = img_list + img_item+ '<br/>'
                }
                else{
                    img_list = img_list + img_item
                }
                count = count + 1
            });

            console.log(JSON.stringify(img_list));
            var div = document.createElement('div');
            div.style.margin = '20px';
            div.innerHTML = img_list
            mycontainer.appendChild(div);
        },
        error: function(data) {
            alert('Request Failed.');
        }
    });
    return false;
}