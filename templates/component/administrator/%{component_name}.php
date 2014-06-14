<?php
/**
 * @version     1.0.0
 * @package     com_%{component_name}
 * @copyright   © 2014. Все права защищены.
 * @license     GNU General Public License версии 2 или более поздней; Смотрите LICENSE.txt
 * @author      %{author_name} <%{author_email}> - %{author_url}
 */


// no direct access
defined('_JEXEC') or die;

// Access check.
if (!JFactory::getUser()->authorise('core.manage', 'com_%{component_name}')) 
{
	throw new Exception(JText::_('JERROR_ALERTNOAUTHOR'));
}

// Include dependancies
jimport('joomla.application.component.controller');

$controller	= JControllerLegacy::getInstance('%{component_name_cap}');
$controller->execute(JFactory::getApplication()->input->get('task'));
$controller->redirect();
