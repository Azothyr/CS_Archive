import os


paths = {
'user': os.path.expanduser('~'),
'documents': os.path.join(os.path.expanduser('~'), 'Documents'),
'custom_scripts': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts'),
'tools': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'script_tools'),
'maya': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts'),
'user_setup': os.path.join(os.path.expanduser('~\\Documents\\maya\\2024\\scripts\\userSetup.py')),
'maya_exe': 'C:\\Program Files\\Autodesk\\Maya2024\\bin',
'arg_maps': {'All': "os.path.join(base_path, 'arg_map.py')", 'button': "os.path.join(base_path, 'button_arg_map.py')", 'columnLayout': "os.path.join(base_path, 'columnLayout_arg_map.py')", 'menuItem': "os.path.join(base_path, 'menuItem_arg_map.py')", 'optionMenu': "os.path.join(base_path, 'optionMenu_arg_map.py')", 'rowColumnLayout': "os.path.join(base_path, 'rowColumnLayout_arg_map.py')", 'tabLayout': "os.path.join(base_path, 'tabLayout_arg_map.py')", 'textField': "os.path.join(base_path, 'textField_arg_map.py')", 'text': "os.path.join(base_path, 'text_arg_map.py')", 'window': "os.path.join(base_path, 'window_arg_map.py')"},
'error': "Invalid Key",
'script_repo': "C:\GitRepos\Scripts_Private\Python\PythonScripts\script_tools",
'maya_repo': "C:\GitRepos\MayaPythonToolbox\maya_scripts",
'maya_components': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'components'),
'maya_info': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'info'),
'maya_tools': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'tools'),
'maya_ui': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'ui'),
'maya_utilities': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'utilities'),
'maya_button_base': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'button_base.py'),
'maya_color_library': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'color_library.py'),
'maya_columnLayout_base': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'columnLayout_base.py'),
'maya_maya_cmds_base': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'maya_cmds_base.py'),
'maya_menuItem_base': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'menuItem_base.py'),
'maya_optionMenu_base': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'optionMenu_base.py'),
'maya_rowColumnLayout_base': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'rowColumnLayout_base.py'),
'maya_tabLayout_base': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'tabLayout_base.py'),
'maya_textField_base': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'textField_base.py'),
'maya_text_base': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'text_base.py'),
'maya_window_base': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'window_base.py'),
'maya_arg_lib': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'arg_lib.py'),
'maya_center_locator': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'center_locator.py'),
'maya_color_changer': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'color_changer.py'),
'maya_constrain_cmds': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'constrain_cmds.py'),
'maya_control_creator': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'control_creator.py'),
'maya_distance_measurment': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'distance_measurment.py'),
'maya_joint_axis_vis_toggle': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'joint_axis_vis_toggle.py'),
'maya_joint_creator': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'joint_creator.py'),
'maya_joint_orient': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'joint_orient.py'),
'maya_layer_control': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'layer_control.py'),
'maya_mirror_cmds': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'mirror_cmds.py'),
'maya_modify_history': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'modify_history.py'),
'maya_parent_cmds': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'parent_cmds.py'),
'maya_selection_renamer': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'selection_renamer.py'),
'maya_select_cmds': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'select_cmds.py'),
'maya_xform_handler': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'xform_handler.py'),
'maya_color_change_ui': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'color_change_ui.py'),
'maya_control_ui': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'control_ui.py'),
'maya_joint_ui': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'joint_ui.py'),
'maya_main_win_tab': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'main_win_tab.py'),
'maya_toolbox_ui': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'toolbox_ui.py'),
'maya_utilities_ui': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'utilities_ui.py'),
'maya_arg_lib_reader': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'arg_lib_reader.py'),
'maya_arg_map_utils': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'arg_map_utils.py'),
'maya_cmds_class_builder': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'cmds_class_builder.py'),
'maya_global_var': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'global_var.py'),
'maya_maya_setup': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'maya_setup.py'),
'maya_selection_check': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'selection_check.py'),
'maya_test_components': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'test_components.py'),
'maya_ui_presence_checker': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts', 'ui_presence_checker.py'),
'tools_components': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'script_tools', 'components'),
'tools_cus_funcs': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'script_tools', 'cus_funcs'),
'tools_info': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'script_tools', 'info'),
'tools_utils': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'script_tools', 'utils'),
'tools_calculator': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'script_tools', 'calculator.py'),
'tools_custom_exception': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'script_tools', 'custom_exception.py'),
'tools_assignment_filler_school': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'script_tools', 'assignment_filler_school.py'),
'tools_file_tools': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'script_tools', 'file_tools.py'),
'tools_format_tool': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'script_tools', 'format_tool.py'),
'tools_get_user_input': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'script_tools', 'get_user_input.py'),
'tools_list_maker': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'script_tools', 'list_maker.py'),
'tools_math_funcs': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'script_tools', 'math_funcs.py'),
'tools_WinDirectoryCopyFile': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'script_tools', 'WinDirectoryCopyFile.py'),
'tools_file_path_library': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'script_tools', 'file_path_library.py'),
'tools_path_map': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'script_tools', 'path_map.py'),
'tools_cmd_handler': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'script_tools', 'cmd_handler.py'),
'tools_map_handler': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'script_tools', 'map_handler.py')
}
