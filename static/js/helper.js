var clipboard_fc = 0;
var links_fc = 0;

function increaseFields(field){
  dom_text = '';
  
  if(field == 'clipboard-text'){
    elem = document.getElementById('clipboard-text-' + clipboard_fc);
    clipboard_fc += 1;
    clipboard_id = 'clipboard-text-' + clipboard_fc;
    dom_text = "<span id='" + clipboard_id + "'><input name='" + clipboard_id + "' style='display: inline; margin-top: 10px' type='text-area' class='form-control' placeholder='Paste text here...'></span>";
  }
  else{
    elem = document.getElementById('link-text-' + clipboard_fc);
    links_fc += 1;
    links_id = 'link-text-' + links_fc;
    dom_text = "<span id='" + links_id + "'><input name='" + links_id +"' style='display: inline; margin-top: 10px' type='text-area' class='form-control' placeholder='Enter link here...'></span>";
  }

    elem.insertAdjacentHTML('beforebegin', dom_text);
}

function decreaseFields(field){
  if(field == 'clipboard-text'){
    if(clipboard_fc>0){          
      elem = document.getElementById('clipboard-text-' + clipboard_fc);
      clipboard_fc -= 1;
      elem.parentNode.removeChild(elem);
    }
  }else{
    if(links_fc>0){          
      elem = document.getElementById('link-text-' + links_fc);
      links_fc -= 1;
      elem.parentNode.removeChild(elem);
    }
  }
}

function openTab(tabName, nav_item){
  var i;
  var x = document.getElementsByClassName("tab");
  var y = document.getElementsByClassName("nav-link");
  
  for (i = 0; i < x.length; i++) {        
    x[i].style.display = "none";
    y[i].classList.remove("active");
    y[i].classList.remove("active-shade");
  }

  document.getElementById(tabName).style.display = "block";
  
  if(nav_item!='search_tab'){    
    if(!document.getElementById('collapseSources').classList.contains("d-none")){
      document.getElementById('collapseSources').classList.add("d-none")
      document.getElementById('sources-button').classList.add("d-none")
    }

    if(nav_item=='clipboard_tab'){
      document.getElementById('link-add').setAttribute('accesskey', '');
      document.getElementById('link-minus').setAttribute('accesskey', '');
      document.getElementById('clipboard-add').setAttribute('accesskey', '+');
      document.getElementById('clipboard-minus').setAttribute('accesskey', '-');
    }else{
      document.getElementById('clipboard-add').setAttribute('accesskey', '');
      document.getElementById('clipboard-minus').setAttribute('accesskey', '');    
      document.getElementById('link-add').setAttribute('accesskey', '+');
      document.getElementById('link-minus').setAttribute('accesskey', '-');      
    }
  }else{
    document.getElementById('clipboard-add').setAttribute('accesskey', '');
    document.getElementById('clipboard-minus').setAttribute('accesskey', '');    
    document.getElementById('link-add').setAttribute('accesskey', '');
    document.getElementById('link-minus').setAttribute('accesskey', '');

    if(document.getElementById('collapseSources').classList.contains("d-none")){
      document.getElementById('collapseSources').classList.remove("d-none")
      document.getElementById('sources-button').classList.remove("d-none")
    }
  }
  
  document.getElementById(nav_item).classList.add("active");
  document.getElementById(nav_item).classList.add("active-shade");
}

function update_sources(source_array){
  var sources = document.getElementById('sources');
  var badge = document.getElementById('sources-badge');
  sources.innerHTML = '';
  var htmlString = '';
  var i = 0;

  if(source_array.length!=0){
    for(i=0; i<source_array[0].length; i++){
      htmlString += '<a href="'+ source_array[1][i] + '" class="list-group-item list-group-item-action list-group-flush" target="_blank">' + '<p style="color: #0056b3">' + source_array[0][i] + '</p>'  + source_array[2][i] + '</a>';      
    }

    sources.innerHTML = htmlString;
    badge.innerHTML = source_array[0].length;
  }
}

function show_mask(opt){
  var id = 'mask';
  if(opt){
    if(document.getElementById(id).classList.contains("d-none")){
     document.getElementById(id).classList.remove("d-none");
    }
  }else{
    if(!document.getElementById(id).classList.contains("d-none")){
     document.getElementById(id).classList.add("d-none");
    }
  }
}


function copy_summary(){
  document.getElementById('summary-area').select();
  document.execCommand('copy');  
  success_clipboard()
}

function success_retrieve(){
  $("#success-alert").fadeTo(2000, 500).slideUp(500, function(){
          $("#success-alert").slideUp(500);
        });
}

function failure_retrieve(){
  $("#failure-alert").fadeTo(2000, 500).slideUp(500, function(){
    $("#failure-alert").slideUp(500);
});
}

function success_clipboard(){
  $("#info-alert").fadeTo(2000, 500).slideUp(500, function(){
    $("#info-alert").slideUp(500);
});
}