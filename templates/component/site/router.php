<?php
/**
 * @version     1.0.0
 * @package     com_%{component_name}
 * @copyright   © 2014. Все права защищены.
 * @license     GNU General Public License версии 2 или более поздней; Смотрите LICENSE.txt
 * @author      %{author_name} <%{author_email}> - %{author_url}
 */

// No direct access
defined('_JEXEC') or die;

/**
 * @param	array	A named array
 * @return	array
 */
function %{component_name_cap}BuildRoute(&$query)
{
	$segments = array();
    
	if (isset($query['task'])) {
		$segments[] = implode('/',explode('.',$query['task']));
		unset($query['task']);
	}
	if (isset($query['id'])) {
		$segments[] = $query['id'];
		unset($query['id']);
	}

	return $segments;
}

/**
 * @param	array	A named array
 * @param	array
 *
 * Formats:
 *
 * index.php?/%{component_name}/task/id/Itemid
 *
 * index.php?/%{component_name}/id/Itemid
 */
function %{component_name_cap}ParseRoute($segments)
{
	$vars = array();
    
	// view is always the first element of the array
	$count = count($segments);
    
    if ($count)
	{
		$count--;
		$segment = array_pop($segments) ;
		if (is_numeric($segment)) {
			$vars['id'] = $segment;
		}
        else{
            $count--;
            $vars['task'] = array_pop($segments) . '.' . $segment;
        }
	}

	if ($count)
	{   
        $vars['task'] = implode('.',$segments);
	}
	return $vars;
}
