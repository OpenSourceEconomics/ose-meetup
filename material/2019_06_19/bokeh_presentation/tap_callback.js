var chosen = source.selected.indices;
if (typeof(chosen) == "number"){
    var chosen = [chosen]
};

var chosen_models = [];

for (var i = 0; i < chosen.length; ++ i){
    chosen_models.push(source.data['model'][chosen[i]])
};

var chosen_models_indices = [];

for (var i = 0; i < source.data['index'].length; ++ i){
    if (chosen_models.includes(source.data['model'][i])){
        chosen_models_indices.push(i)
    };
};

source.selected.indices = chosen_models_indices;
source.change.emit();