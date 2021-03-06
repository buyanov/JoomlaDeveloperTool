<?php
/**
 * @version     1.0.0
 * @package     com_%{component_name}
 * @copyright   © 2014. Все права защищены.
 * @license     GNU General Public License версии 2 или более поздней; Смотрите LICENSE.txt
 * @author      %{author_name} <%{author_email}> - %{author_url}
 */

defined('_JEXEC') or die;

// Include dependancies
jimport('joomla.application.component.controller');

// Execute the task.
$controller	= JControllerLegacy::getInstance('%{component_name_cap}');
$controller->execute(JFactory::getApplication()->input->get('task'));
$controller->redirect();
