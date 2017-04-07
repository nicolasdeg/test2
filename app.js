var app = angular.module('app', ['ngAnimate', 'ngTouch', 'ui.grid', 'ui.grid.selection', 'ui.grid.resizeColumns', 'ui.grid.moveColumns']);

app.controller('MainCtrl', ['$scope', '$http','uiGridConstants',  function ($scope, $http ,uiGridConstants) {


  $scope.gridOptions = {
	showGridFooter: true,
    showColumnFooter: true,
    enableFiltering: true,
	enableSorting: true,
    onRegisterApi: function(gridApi){
      $scope.gridApi = gridApi;
    },
    columnDefs: [
      { field: 'service_rh'},
      { field: 'id_nat_frt' },
      { field: 'cle_frt_mini' },
      { field: 'surface_cadastrale',aggregationType: uiGridConstants.aggregationTypes.avg, aggregationHideLabel: true},
      { field: 'domanial' },
      { field: 'cadre_legal_gestion' },
      { field: 'type_copropriete' },
      { field: 'proprio_categorie' },
      { field: 'libelle_usage' },
      { field: 'departement_majoritaire' },
      { field: 'date_debut_validite' },
      { field: 'date_fin_validite' }
    ]
	
  };
  $scope.toggleFooter = function() {
    $scope.gridOptions.showGridFooter = !$scope.gridOptions.showGridFooter;
    $scope.gridApi.core.notifyDataChange(uiGridConstants.dataChange.OPTIONS);
    };

  $scope.toggleColumnFooter = function() {
    $scope.gridOptions.showColumnFooter = !$scope.gridOptions.showColumnFooter;
    $scope.gridApi.core.notifyDataChange(uiGridConstants.dataChange.OPTIONS);
  };
  
  $http.get('https://raw.githubusercontent.com/nicolasdeg/test2/master/starter18.json')
    .success(function(data) {
      $scope.gridOptions.data = data;
    });
}])