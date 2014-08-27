module.exports = function (grunt) {
  grunt.loadNpmTasks('grunt-recess');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-clean');

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    builddir: 'build',
    meta: {
      banner: '/**\n' +
              ' * <%= pkg.description %>\n' +
              ' * @version v<%= pkg.version %> - ' +
              '<%= grunt.template.today("yyyy-mm-dd") %>\n' +
              ' * @link <%= pkg.homepage %>\n' +
              ' * @license <%= pkg.license %>' + ' */'
    },
    swatch: {
      amelia:{}, cerulean:{}, cosmo:{}, cyborg:{}, flatly:{}, journal:{}, readable:{},
      simplex:{}, slate:{}, spacelab:{}, spruce:{}, superhero:{}, united:{}
    },
    clean: {
      build: {
        src: ['*/build.less', '*/build-responsive.less',
              '!global/build.less', '!global/build-responsive.less']
      }
    },
    concat: {
      dist: {
        src: [],
        dest: ''
      }
    },
    recess: {
      dist: {
        options: {
          compile: true,
          compress: false
        },
        files: {}
      }
    }
  });

  grunt.registerTask('none', function() {});

  grunt.registerTask('build', 'build a regular theme', function(theme, compress) {
    var compress = compress == undefined ? true : compress;

    var concatSrc;
    var concatDest;
    var recessDest;
    var recessSrc;
    var files = {};
    var dist = {};
    concatSrc = 'global/build.less';
    concatDest = theme + '/build.less';
    recessDest = '<%=builddir%>/' + theme + '/bootstrap.css';
    recessSrc = [ theme + '/' + 'build.less' ];

    dist = {src: concatSrc, dest: concatDest};
    grunt.config('concat.dist', dist);
    files = {}; files[recessDest] = recessSrc;
    grunt.config('recess.dist.files', files);
    grunt.config('recess.dist.options.compress', false);

    grunt.task.run(['concat', 'recess:dist', 'clean:build',
      compress ? 'compress:'+recessDest+':'+'<%=builddir%>/' + theme + '/bootstrap.min.css':'none']);
  });

  grunt.registerTask('build-responsive', 'build a responsive theme', function(theme, compress) {
    var compress = compress == undefined ? true : compress;

    var concatSrc;
    var concatDest;
    var recessDest;
    var recessSrc;
    var files = {};
    var dist = {};

    concatSrc = 'global/build-responsive.less';
    concatDest = theme + '/build-responsive.less';
    recessDest = '<%=builddir%>/' + theme + '/bootstrap-responsive.css';
    recessSrc = [ theme + '/' + 'build-responsive.less' ];

    dist = {src: concatSrc, dest: concatDest};
    grunt.config('concat.dist', dist);
    files = {}; files[recessDest] = recessSrc;
    grunt.config('recess.dist.files', files);
    grunt.config('recess.dist.options.compress', false);

    grunt.task.run(['concat', 'recess:dist', 'clean:build',
      compress ? 'compress:'+recessDest+':'+'<%=builddir%>/' + theme + '/bootstrap-responsive.min.css':'none']);
  });

  grunt.registerTask('compress', 'compress a generic css', function(fileSrc, fileDst) {
    var files = {}; files[fileDst] = fileSrc;
    grunt.log.writeln('compressing file ' + fileSrc);

    grunt.config('recess.dist.files', files);
    grunt.config('recess.dist.options.compress', true);
    grunt.task.run(['recess:dist']);
  });

  grunt.registerMultiTask('swatch', 'build a theme, both not responsive and responsive', function() {
    var t = this.target;
    grunt.task.run('build:'+t, 'build-responsive:'+t);
  });

  grunt.registerTask('default', 'build a theme, both not responsive and responsive', function() {
    grunt.task.run('swatch');
  });
};