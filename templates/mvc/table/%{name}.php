<?php
/**
 * @version     %{version}
 * @package     com_%{component_name}
 * @copyright   %{author_copyright}
 * @license     %{author_license}
 * @author      %{author_name} <%{author_email}> - %{author_url}
 */

defined('_JEXEC') or die;

class %{component_name_cap}Table%{name_cap} extends JTable
{
	public function __construct(&$_db)
	{
		parent::__construct('#__%{component_name}_%{name}', 'id', $_db);
	}
	
}